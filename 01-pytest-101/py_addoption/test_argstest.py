def test_argstest(CmdOpt):
    # print("Read config file: " + CmdOpt.readline())
    assert CmdOpt.readline().index("Lab")
