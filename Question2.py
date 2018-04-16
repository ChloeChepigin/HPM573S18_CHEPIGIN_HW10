# Question 2

# Estimate the change in the expected discounted cost, the expected discounted utility, and
# expected number of strokes when the anticoagulation drug is used

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
simOutputs_notreatment = cohortnotreatment.simulate()

# create a cohort for the anticoagulant
cohortanticoag = MarkovCls.Cohort(
    id=1,
    therapy=P.Therapies.ANTICOAG
)
simOutputs_Anticoag = cohortanticoag.simulate()


# print comparative outcomes
SupportMarkov.print_comparative_outcomes(simOutputs_notreatment, simOutputs_Anticoag)