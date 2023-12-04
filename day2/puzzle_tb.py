import cocotb
from cocotb.triggers import RisingEdge, FallingEdge, ClockCycles, Timer
from cocotb.clock import Clock

def input_prep(input_file):
    games = []
    with open(input_file, "r") as f:
        for line in f:
            game = line.split(":")[-1].strip()
            rounds = []
            for g_rounds in game.split(";"):
                draw = {}
                for cube in g_rounds.split(", "):
                    cube = cube.strip().split(" ")
                    draw[cube[1]] = int(cube[0])
                rounds.append(draw)
            games.append(rounds)
    return games

@cocotb.test()
async def test_puzzle(dut):

    input_file = input_prep("input.txt")

    dut.clk_i.value = 0
    dut.rstn_i.value = 1
    dut.run_i.value = 0
    dut.new_game_i.value = 0
    dut.red_cubes_i.value = 0
    dut.green_cubes_i.value = 0
    dut.blue_cubes_i.value = 0

    cocotb.start_soon(Clock(dut.clk_i, 1, units="ns").start())  # run the clock "in the background"

    # Reset
    await RisingEdge(dut.clk_i)
    dut.rstn_i.value = 0
    await ClockCycles(dut.clk_i, 2) # Hold reset for 2 clock cycles
    dut.rstn_i.value = 1

    # Start processing
    dut.run_i.value = 1
    dut.new_game_i.value = 1
    for game in input_file:
        for draw in game:
            await RisingEdge(dut.clk_i)
            dut.red_cubes_i.value = draw.get("red", 0)
            dut.green_cubes_i.value = draw.get("green", 0)
            dut.blue_cubes_i.value = draw.get("blue", 0)
            dut.new_game_i.value = 0

        # Start new game
        await RisingEdge(dut.clk_i)
        dut.new_game_i.value = 1
        dut.red_cubes_i.value = 0
        dut.green_cubes_i.value = 0
        dut.blue_cubes_i.value = 0


    # Stop processing
    await RisingEdge(dut.clk_i)
    dut.run_i.value = 0

    await Timer(5, units="ns") # Wait a bit, just for the looks of the waveform

    print(f"Puzzle Result: {int(dut.sum_o.value)}")
