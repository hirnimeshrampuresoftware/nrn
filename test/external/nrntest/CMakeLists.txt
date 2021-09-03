# Set up tests from the nrntest external repository
include(NeuronTestHelper)

# Step 1 -- define a group of configurations
nrn_add_test_group(
  NAME external_nrntest
  SUBMODULE tests/nrntest)

# Step 2 -- define a new test
nrn_add_test(
  GROUP external_nrntest
  NAME nrntest
  COMMAND bash runtests)

