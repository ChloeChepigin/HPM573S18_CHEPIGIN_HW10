# Question 1

# Estimate the discounted total cost and discounted total utility of
# patients who start in "Well"

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
    id=1,
    therapy=P.Therapies.ANTICOAG
)
simOutputs_Anticoag = cohortanticoag.simulate()

# prints the outcomes (means and CI)
SupportMarkov.print_outcomes(simOutputs_Notreatment, 'No Treatment')
SupportMarkov.print_outcomes(simOutputs_Anticoag, 'Treatment/Anticoagulant')