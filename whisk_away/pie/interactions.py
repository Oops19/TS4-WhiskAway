
from typing import Any

from interactions.context import InteractionContext
from sims.sim import Sim
from sims4.tuning.tunable import Tunable
from sims4communitylib.classes.interactions.common_immediate_super_interaction import CommonImmediateSuperInteraction
from sims4communitylib.classes.testing.common_test_result import CommonTestResult
from sims4communitylib.utils.common_log_registry import CommonLog, CommonLogRegistry
from sims4communitylib.utils.common_type_utils import CommonTypeUtils
from sims4communitylib.utils.sims.common_sim_utils import CommonSimUtils
from whisk_away.modinfo import ModInfo
from whisk_away.whisk_away_action import WhiskAwayAction

log: CommonLog = CommonLogRegistry().register_log(ModInfo.get_identity(), 'InteractionsWhiskAway')
log.enable()


class InteractionsWhiskAway(CommonImmediateSuperInteraction):
    INSTANCE_TUNABLES = {
        'whisk_id': Tunable(tunable_type=int, default=0),
    }

    __slots__ = {'whisk_id', }

    @classmethod
    def on_test(cls, interaction_sim: Sim, interaction_target: Any, interaction_context: InteractionContext, **kwargs) -> CommonTestResult:
        source_sim_info = CommonSimUtils.get_sim_info(interaction_sim)
        if not CommonTypeUtils.is_sim_instance(interaction_target):
            return CommonTestResult.NONE
        target_sim_info = CommonSimUtils.get_sim_info(interaction_target)
        if source_sim_info.id == target_sim_info.id:
            return CommonTestResult.NONE
        r'''
        if CommonAgeUtils.is_baby_infant_toddler_or_child(source_sim_info):
            Check for crazy trait which doesn't exist.
        '''

        return CommonTestResult.TRUE

    def on_started(self, interaction_sim: Sim, interaction_target: Any) -> bool:
        log.debug(f"on_started({interaction_sim}, {interaction_target}, whisk_id={getattr(self, 'whisk_id')}, )")
        return WhiskAwayAction().whisk_away(self, interaction_sim, interaction_target)
