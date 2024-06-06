
from typing import Tuple
from objects.script_object import ScriptObject
from sims4communitylib.services.interactions.interaction_registration_service import CommonInteractionRegistry, CommonInteractionType, CommonScriptObjectInteractionHandler
from sims4communitylib.utils.common_type_utils import CommonTypeUtils


@CommonInteractionRegistry.register_interaction_handler(CommonInteractionType.ON_SCRIPT_OBJECT_LOAD)
class RegisterInteractionsWhiskAwayWhisk_Away0(CommonScriptObjectInteractionHandler):
    @property
    def interactions_to_add(self) -> Tuple[int]:
        interactions: Tuple = (
            0x010D4DFF8A02FBD5,  # 'To Super-Nanny' - fnv('o19_Whisk_Away_PMC__Whisk_Away_PMA_To_Superx2DNanny_debug')
            0xA4EBB300C29350E7,  # 'Sell to Family' - fnv('o19_Whisk_Away_PMC__Whisk_Away_PMA_Sell_to_Family_debug')
            0xFCD3E0E38B187E5B,  # 'Baby Hatch' - fnv('o19_Whisk_Away_PMC__Whisk_Away_PMA_Baby_Hatch_debug')
            0x8D4DB2F8A078CC5A,  # 'Throw into Wishing Well' - fnv('o19_Whisk_Away_PMC__Whisk_Away_PMA_Throw_into_Wishing_Well_debug')
            0xB324F13D154E141B,  # 'Tie to the dog kennel' - fnv('o19_Whisk_Away_PMC__Whisk_Away_PMA_Tie_to_the_dog_kennel_debug')
            0x68A055AFF0E780A6,  # 'Throw into Dumpster' - fnv('o19_Whisk_Away_PMC__Whisk_Away_PMA_Throw_into_Dumpster_debug')
            0x48D249E036F06BD3,  # 'Send to end of the rainbow' - fnv('o19_Whisk_Away_PMC__Whisk_Away_PMA_Send_to_end_of_the_rainbow_debug')
            0x998A5663457634D4,  # 'Lock in closet and throw key away' - fnv('o19_Whisk_Away_PMC__Whisk_Away_PMA_Lock_in_closet_and_throw_key_away_debug')
            0x77D7D86BDD1F942F,  # 'Abandon in forest' - fnv('o19_Whisk_Away_PMC__Whisk_Away__Go_west_PMA_Abandon_in_forest_debug')
            0x14547D33E98F028F,  # 'Drown in Bathtub' - fnv('o19_Whisk_Away_PMC__Whisk_Away__Go_west_PMA_Drown_in_Bathtub_debug')
            0x93463C182077DC4E,  # 'Burn in Oven' - fnv('o19_Whisk_Away_PMC__Whisk_Away__Go_west_PMA_Burn_in_Oven_debug')
            0x44B74FC7DF6D5465,  # 'Freeze in Fridge' - fnv('o19_Whisk_Away_PMC__Whisk_Away__Go_west_PMA_Freeze_in_Fridge_debug')
            0x4F14B3B0BDBD54A2,  # 'Feed the Pigs' - fnv('o19_Whisk_Away_PMC__Whisk_Away__Go_west_PMA_Feed_the_Pigs_debug')
            0xFD905016C5D1C8D4,  # 'Bury Alive' - fnv('o19_Whisk_Away_PMC__Whisk_Away__Go_west_PMA_Bury_Alive_debug')
            0x941A34F49756E598,  # 'Stuffing the sim' - fnv('o19_Whisk_Away_PMC__Whisk_Away__Go_west_PMA_Stuffing_the_sim_debug')
            0x816F464ECF3B0C71,  # 'Eat {1.SimFirstName}' - fnv('o19_Whisk_Away_PMC__Whisk_Away__Go_west_PMA_Eat__1_SimFirstName__debug')
            0x8B45AACC95A03166,  # 'Chop wood' - fnv('o19_Whisk_Away_PMC__Whisk_Away__Go_west_PMA_Chop_wood_debug')
            0x76CFB03172B9C522,  # 'Throw to lions' - fnv('o19_Whisk_Away_PMC__Whisk_Away__Go_west_PMA_Throw_to_lions_debug')
            0xD1DD7CBE1A0AEC98,  # 'Give toy to play with' - fnv('o19_Whisk_Away_PMC__Whisk_Away__Go_west_PMA_Give_toy_to_play_with_debug')
            0x581E096C1313027F,  # 'Tickle to death' - fnv('o19_Whisk_Away_PMC__Whisk_Away__Go_west_PMA_Tickle_to_death_debug')
            0x468622F0A04707B5,  # 'Scare to death' - fnv('o19_Whisk_Away_PMC__Whisk_Away__Go_west_PMA_Scare_to_death_debug')
            0x67F3D9253455CA15,  # 'Rest In Peace' - fnv('o19_Whisk_Away_PMC__Whisk_Away__Eternal_Void_PMA_Rest_In_Peace_debug')
            0xA8F1406C6E5F2FBE,  # 'Donate blood' - fnv('o19_Whisk_Away_PMC__Whisk_Away__Eternal_Void_PMA_Donate_blood_debug')
            0x16B6BB16305A92F4,  # 'Play with Voodoo Doll' - fnv('o19_Whisk_Away_PMC__Whisk_Away__Eternal_Void_PMA_Play_with_Voodoo_Doll_debug')
            0x1D1D22F522097D9B,  # 'Alien abduction' - fnv('o19_Whisk_Away_PMC__Whisk_Away__Eternal_Void_PMA_Alien_abduction_debug')
            0xAA82DA4CCAB77EB7,  # 'Send to outer space' - fnv('o19_Whisk_Away_PMC__Whisk_Away__Eternal_Void_PMA_Send_to_outer_space_debug')
            0xC6BFE0E2C8DD8B88,  # 'Feed the Cow Plant' - fnv('o19_Whisk_Away_PMC__Whisk_Away__Eternal_Void_PMA_Feed_the_Cow_Plant_debug')
            0xCBB15E8B83BF71E9,  # 'Put in Murphy Bed' - fnv('o19_Whisk_Away_PMC__Whisk_Away__Eternal_Void_PMA_Put_in_Murphy_Bed_debug')
            0xEA8218B2ED815EF0,  # 'Arrange meeting with Death' - fnv('o19_Whisk_Away_PMC__Whisk_Away__Eternal_Void_PMA_Arrange_meeting_with_Death_debug')
            0x5D58F2E55F1E3D11,  # 'Invite to play with shark' - fnv('o19_Whisk_Away_PMC__Whisk_Away__Eternal_Void_PMA_Invite_to_play_with_shark_debug')
            0x5BEBC618429638EE,  # 'Poison' - fnv('o19_Whisk_Away_PMC__Whisk_Away__Eternal_Void_PMA_Poison_debug')
            0x47111386E4797702,  # 'Throw out of plane' - fnv('o19_Whisk_Away_PMC__Whisk_Away__Eternal_Void_PMA_Throw_out_of_plane_debug')
            0x74A02578EEAFA876,  # 'Put alive in hanging coffin' - fnv('o19_Whisk_Away_PMC__Whisk_Away__Eternal_Void_PMA_Put_alive_in_hanging_coffin_debug')
            0xA9DD36B3A0A7644C,  # 'Electrocution' - fnv('o19_Whisk_Away_PMC__Whisk_Away__Eternal_Void_PMA_Electrocution_debug')
            0xF1097B24B625081A,  # 'Exterminate this race' - fnv('o19_Whisk_Away_PMC__Whisk_Away__Bad_Religion_PMA_Exterminate_this_race_debug')
            0xCC201857D5FA5796,  # 'Exterminate this gender' - fnv('o19_Whisk_Away_PMC__Whisk_Away__Bad_Religion_PMA_Exterminate_this_gender_debug')
            0xF84AF7B9E0F4C013,  # 'Exterminate this body shape' - fnv('o19_Whisk_Away_PMC__Whisk_Away__Bad_Religion_PMA_Exterminate_this_body_shape_debug')
            0x3A63737F84C4DAF9,  # 'Exterminate this voice' - fnv('o19_Whisk_Away_PMC__Whisk_Away__Bad_Religion_PMA_Exterminate_this_voice_debug')
            0xF21955F7CB91CC0C,  # 'Exterminate this look' - fnv('o19_Whisk_Away_PMC__Whisk_Away__Bad_Religion_PMA_Exterminate_this_look_debug')
            0xB98F0D1003BD7735,  # 'Exterminate this breed' - fnv('o19_Whisk_Away_PMC__Whisk_Away__Bad_Religion_PMA_Exterminate_this_breed_debug')
        )
        return interactions

    def should_add(self, script_object: ScriptObject, *args, **kwargs) -> bool:
        return CommonTypeUtils.is_sim_instance(script_object)
