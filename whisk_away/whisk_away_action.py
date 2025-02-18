import random

from sims.genealogy_tracker import FamilyRelationshipIndex
from sims.sim_info import SimInfo
from sims4communitylib.classes.testing.common_execution_result import CommonExecutionResult
from sims4communitylib.enums.tags_enum import CommonGameTag
from sims4communitylib.notifications.common_basic_notification import CommonBasicNotification
from sims4communitylib.utils.common_log_registry import CommonLog, CommonLogRegistry
from sims4communitylib.utils.resources.common_skill_utils import CommonSkillUtils
from sims4communitylib.utils.sims.common_age_utils import CommonAgeUtils
from sims4communitylib.utils.sims.common_gender_utils import CommonGenderUtils
from sims4communitylib.utils.sims.common_sim_spawn_utils import CommonSimSpawnUtils
from sims4communitylib.utils.sims.common_sim_utils import CommonSimUtils
from statistics.skill import Skill


import services
import sims4
import sims4.resources
import sims4.commands
from sims.household_enums import HouseholdChangeOrigin
from sims4communitylib.utils.sims.common_household_utils import CommonHouseholdUtils
from sims4communitylib.utils.sims.common_trait_utils import CommonTraitUtils
from ui.ui_dialog_notification import UiDialogNotification
from whisk_away.enums.wa_ids import WhiskAwayIDs
from whisk_away.modinfo import ModInfo

log: CommonLog = CommonLogRegistry.get().register_log(ModInfo.get_identity(), ModInfo.get_identity().name)
log.enable()


class WhiskAwayAction:
    def whisk_away(self, interaction, interaction_sim, interaction_target) -> CommonExecutionResult:
        errors = False
        interaction_id = 0
        target_sim_info: SimInfo = None
        try:
            source_sim_info = CommonSimUtils.get_sim_info(interaction_sim)
            target_sim_info = CommonSimUtils.get_sim_info(interaction_target)
            r"""
            Assume that teems have enough power to commit all actions.
            And assume that babies-children will take care only of same age or younger ages.
            """
            if CommonAgeUtils.is_child(source_sim_info):
                if not CommonAgeUtils.is_baby_infant_toddler_or_child(target_sim_info):
                    log.debug(':-( Search a younger target, child! )-:')
                    return CommonExecutionResult.TRUE  # Do nothing
            if CommonAgeUtils.is_toddler(source_sim_info):
                if not CommonAgeUtils.is_baby_infant_or_toddler(target_sim_info):
                    log.debug(':-( Search a younger target, toddler! )-:')
                    return CommonExecutionResult.TRUE  # Do nothing
            if CommonAgeUtils.is_infant(source_sim_info):
                if not (CommonAgeUtils.is_baby(target_sim_info) or CommonAgeUtils.is_infant(target_sim_info)):
                    log.debug(':-( Search a younger target, infant! )-:')
                    return CommonExecutionResult.TRUE  # Do nothing
            if CommonAgeUtils.is_baby(source_sim_info):
                log.debug(":-( You're a baby. What do you know about virtual life? )-:")
                return CommonExecutionResult.TRUE  # Do nothing

            if CommonAgeUtils.is_baby_infant_toddler_or_child(target_sim_info):
                """ Only allow parents to purge sims """
                """ Only allow mean+mischief sims to purge sims """
                mother_sim_id = target_sim_info.get_relation(FamilyRelationshipIndex.MOTHER)
                mother_sim_info = CommonSimUtils.get_sim_info(mother_sim_id)
                father_sim_id = target_sim_info.get_relation(FamilyRelationshipIndex.FATHER)
                father_sim_info = CommonSimUtils.get_sim_info(father_sim_id)

                log.debug(f"{mother_sim_id} {mother_sim_info} - {father_sim_id} {father_sim_info}")
                # In case father is None let's assume that whichever sim is running the interaction it is the father
                # I saw this too often ... sims with just one parent (mother) due to TS4 issues.
                if father_sim_id is not None and source_sim_info != mother_sim_info and source_sim_info != father_sim_info:
                    log.debug("Source actor is neither father nor mother. Has it enough mischief to steal babies from other sims?")
                    mischief_skill: Skill = CommonSkillUtils.load_skill_by_id(CommonGameTag.SKILL_MISCHIEF.value)
                    if mischief_skill:
                        mischief_skill_level = mischief_skill.get_value
                        if mischief_skill_level < 5:
                            log.debug(f"Source has {mischief_skill_level} mischief which is luckily not enough to continue.")
                            return CommonExecutionResult.TRUE
                    else:
                        log.debug(f"Source has luckily no mischief, we will not abduct the baby.")
                        return CommonExecutionResult.TRUE

            interaction_id = getattr(interaction, 'whisk_id')
            household = None

            if interaction_id == 3:
                # Fate, Throw sim-object into ... Super-Nanny or Family
                interaction_id = random.randint(1, 2)
                log.debug(f"Sim will be integrated into a new live within {'Super-Nanny' if interaction_id == 1 else 'a Family'}.")

            if interaction_id == 2:
                # Family
                household = self._get_family_household(source_sim_info)
                if household is None:
                    log.debug(f"No family household found, looking for Super-Nanny")
                    interaction_id = 1
            if interaction_id == 1:
                # Super-Nanny
                household = self._get_super_nanny_household()
                if household is None:
                    log.debug(f"No household with a Super-Nanny found, sparing the sim this time.")
                    return CommonExecutionResult.TRUE
            elif interaction_id < 0:
                # Go West
                household = CommonHouseholdUtils.create_empty_household()
                if household is None:
                    log.debug(f"Failed to create temporarily household, sparing the sim this time.")
                    return CommonExecutionResult.TRUE
            else:
                log.debug(f"Wrong interaction_id {interaction_id}.")
                return CommonExecutionResult.TRUE

            # Here we have a household and move the sim into it.
            try:
                # Hide the sim immediately, this should also work no matter what happens next even though it doesn't.
                # Sims don't need a reset and can finish their work before they are completely removed
                manager = services.object_manager()
                obj = manager.get(target_sim_info.id)
                obj.fade_opacity(opacity=0.2, duration=0.2)  # Hide the sim, it will still be around if further steps fail
            except:
                pass

            try:
                CommonHouseholdUtils.move_sim_to_household(target_sim_info, household_id=household.id, destroy_if_empty_household=True)
                CommonSimSpawnUtils.despawn_sim(target_sim_info)
            except Exception as e:
                errors = True
                log.warn(f"Oops: '{e}' - Could not move sim to new household")

            # Destroy the sim permanently
            if interaction_id == -1:
                try:
                    # CommonHouseholdUtils.delete_household(household)
                    household.set_to_hidden()
                    target_sim_info.remove_permanently(household=household)
                except Exception as e:
                    errors = True
                    log.warn(f"Oops: '{e}' - Could not destroy sim properly")
            if errors is False:
                self._show_notification(interaction_id, target_sim_info)
        except Exception as e:
            errors = True
            log.error(f"Oops: '{e}'")

        return CommonExecutionResult.TRUE

    @staticmethod
    def _get_family_household(skip_this_sim: SimInfo):
        skip_this_household = CommonHouseholdUtils.get_household(skip_this_sim)
        household = None
        try:
            log.debug(f"Searching for family ...")
            for _household in CommonHouseholdUtils.get_all_households_generator():
                if _household == skip_this_household:
                    continue
                found_mother = False
                found_father = False
                for sim_info in CommonHouseholdUtils.get_household_members_from_household_gen(_household):
                    CommonHouseholdUtils.is_part_of_active_household()
                    if CommonAgeUtils.is_teen_or_young_adult(sim_info):
                        if CommonGenderUtils.is_female(sim_info):
                            found_mother = True
                        elif CommonGenderUtils.is_male(sim_info):
                            found_father = True
                        if found_father and found_mother:
                            household = _household
                            break
                if household:
                    break
            if household:
                log.debug(f"Found household '{household}'.")
            else:
                log.debug(f"No family found")
        except Exception as e:
            log.error(f"Error: '{e}'", throw=False)
        return household

    @staticmethod
    def _get_super_nanny_household():
        household = None
        sim_info = None
        o19_HH_template_female_nanny = WhiskAwayIDs.o19_HH_template_female_nanny.value
        o19_trait_Hidden_Super_Nanny_id = WhiskAwayIDs.o19_trait_Hidden_Super_Nanny_id.value
        try:
            log.debug(f"Searching Super-Nanny ...")
            for sim_info in CommonSimUtils.get_sim_info_for_all_sims_generator():
                if CommonTraitUtils.has_trait(sim_info, o19_trait_Hidden_Super_Nanny_id) and CommonHouseholdUtils.get_free_household_slots(sim_info) >= 1:
                    household = CommonHouseholdUtils.get_household(sim_info)
                    break
            if household is None:
                log.debug(f"Creating new Super-Nanny ...")
                template_id = o19_HH_template_female_nanny
                manager = services.get_instance_manager(sims4.resources.Types.SIM_TEMPLATE)
                template = manager.get(template_id)
                household = template.create_household(None, creation_source='Looking for Super-Nanny', household_change_origin=HouseholdChangeOrigin.CHEAT_FILTER_CREATE_HOUSEHOLD_FROM_TEMP)
                for sim_info in CommonHouseholdUtils.get_sim_info_of_all_sims_in_household_generator(household):
                    if CommonTraitUtils.has_trait(sim_info, o19_trait_Hidden_Super_Nanny_id) and CommonHouseholdUtils.get_free_household_slots(sim_info) >= 1:
                        break
            if household:
                log.debug(f"Found household '{household}' with Super-Nanny")
            else:
                log.debug(f"No Super-Nanny found")

        except Exception as e:
            log.error(f"Error: '{e}'", throw=False)
        return household

    @staticmethod
    def _show_notification(interaction_id: int, sim_info: SimInfo):
        r"""
        @param interaction_id:
        @param sim_info:
        @return:
        """
        if interaction_id == -2:
            title_id = f"O19_WHISK_AWAY_STBL_TITLE_BAD_RELIGION"
            message_id = f"O19_WHISK_AWAY_STBL_BAD_RELIGION_{random.randint(1, 10)}"
        elif interaction_id == -1:
            title_id = f"O19_WHISK_AWAY_STBL_TITLE_DEATH_{random.randint(1, 3)}"
            message_id = f"O19_WHISK_AWAY_STBL_DEATH_{random.randint(1, 20)}"
        else:
            title_id = f"O19_WHISK_AWAY_STBL_TITLE_NEW_HOUSEHOLD_{random.randint(1, 3)}"
            message_id = f"O19_WHISK_AWAY_STBL_NEW_HOUSEHOLD_{random.randint(1, 10)}"

        basic_notification = CommonBasicNotification(
            title_identifier=WhiskAwayIDs[title_id].value,  # "RIP"
            description_identifier=WhiskAwayIDs[message_id].value,  # "{1.SimFirstName} enjoys the silence."
            title_tokens=(),
            description_tokens=(sim_info, ),
            urgency=UiDialogNotification.UiDialogNotificationUrgency.DEFAULT
        )
        basic_notification.show()
