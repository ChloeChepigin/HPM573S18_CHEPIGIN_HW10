# Question 3

# Use a cost-utility plane to display the expected discounted incremental utility and cost
# report the results of the cost-utility analysis

import ParameterClasses as P
import MarkovModelClasses as MarkovCls
import SupportMarkovModel as SupportMarkov
import scr.SamplePathClasses as PathCls
import scr.FigureSupport as Figs

# create cohort for no treatment
cohortnotreatment = MarkovCls.Cohort(
    id=0,
    therapy=P.Therapies.NONE
)
simOutputs_Notreatment = cohortnotreatment.simulate()

# create a cohort for the anticoagulant
cohortanticoag = MarkovCls.Cohort(
    id=3,
    therapy=P.Therapies.ANTICOAG
)
simOutputs_Anticoag = cohortanticoag.simulate()


# report the CEA results
SupportMarkov.report_CEA_CBA(simOutputs_Anticoag, simOutputs_Notreatment)

