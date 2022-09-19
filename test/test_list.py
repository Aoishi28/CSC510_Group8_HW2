def test_list(self, eg, runs, fails):
        print("\nExamples lua csv -e ...")
        for key, values in eg.items():
            print("\t{key}".format(key = key))
        return True