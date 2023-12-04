import random
import cocotb
from cocotb.triggers import RisingEdge, FallingEdge, ClockCycles, Timer
from cocotb.clock import Clock
from cocotb.types import LogicArray
from cocotb.binary import BinaryValue

def parse_input(input_file):
    with open(input_file, "r") as f:
        games = []
        for line in f:
            game = {}
            game["winning"] = [int(x) for x in line.split("|")[0].split(":")[1].split()]
            game["played"] = [int(x) for x in line.split("|")[1].split()]
            games.append(game)

    return games

@cocotb.test()
async def test_puzzle(dut):

    input_file = parse_input("input.txt")

    dut.clk_i.value = 0;
    dut.rstn_i.value = 1;
    dut.run_i.value = 0;

    cocotb.start_soon(Clock(dut.clk_i, 1, units="ns").start())  # run the clock "in the background"

    # Reset
    await RisingEdge(dut.clk_i)
    dut.rstn_i.value = 0;
    await ClockCycles(dut.clk_i, 2) # Hold reset for 2 clock cycles
    dut.rstn_i.value = 1;

    # Start processing
    for game in input_file:
        await RisingEdge(dut.clk_i)
        dut.run_i.value = 1;
        dut.winning_numbers_i.value = BinaryValue(''.join(format(num, "07b") for num in game["winning"]))
        dut.played_numbers_i.value = BinaryValue(''.join(format(num, "07b") for num in game["played"]))

    # Stop processing
    await RisingEdge(dut.clk_i)
    dut.run_i.value = 0;

    await Timer(5, units="ns") # Wait a bit, just for the looks of the waveform

    print(f"Puzzle Result: {int(dut.sum_o.value)}")