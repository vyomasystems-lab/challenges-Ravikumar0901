# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""

    cocotb.log.info('##### CTB: Develop your test here ########')
    """Test for input as 1101 """
    S=1101
    #input Driving
    dut.sel.value = S

    await Timer(2,units='2')
    assert dut.out.value == inp13,f"Mux Result is incorrect: {dut.X.value}!=13"

    @cocotb.test()
    async def mux_randomised_test(dut):
        """Test For Selecting random input multiple times"""
        for i in range(5)
             S=random.randinp(0,30)
             dut.sel.value=S
             await Timer(2,units='ns')
             dut._log.info(f'S={S:05} model={out:05} DUT={int(dut.out.value):05}')
             assert dut.out.value == out,"Randomised test failed with: {sel}={outi}".format
             (S=dut.sel.value, outi=dut.out.value)
