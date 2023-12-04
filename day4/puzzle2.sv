/*
 * Advent of Code 2023 - Day 4
 * Puzzle 2
 *
 * The module receives a list of winning numbers, and a list of played numbers, each cycle (a game).
 * The N matching numbers on the current game, provide an extra copy of each of the next N games.
 * The module outputs the number of games played.
*/

`timescale 1us/1ns

module puzzle2
#(
    parameter int WINNING_NUMBERS = 10,
              int PLAYED_NUMBERS = 25,
              int GAMES = 197
)
(
    input logic clk_i,
    input logic rstn_i,
    input logic run_i,
    input logic [WINNING_NUMBERS-1:0][6:0] winning_numbers_i,
    input logic [PLAYED_NUMBERS-1:0][6:0] played_numbers_i,
    output logic [31:0] sum_o
);

logic [GAMES-1:0][31:0]             games;
logic [$clog2(WINNING_NUMBERS)-1:0] matched;
logic [$clog2(GAMES)-1:0]           current_game;
logic [31:0]                        sum;

// Games counter
always_comb begin
    matched = 0;
   if (run_i) begin
        for (int i = 0; i < WINNING_NUMBERS; i++) begin
            for (int j = 0; j < PLAYED_NUMBERS; j++) begin
                if (winning_numbers_i[i] == played_numbers_i[j]) begin
                    matched++;
                end
            end
        end
    end
end

// Game counter
always_ff @(posedge clk_i, negedge rstn_i) begin
    if (!rstn_i) begin
        current_game <= '0;
        for (int i = 0; i < GAMES; i++) begin
            games[i] <= 1;
        end
    end else if (run_i) begin
        for (logic [$clog2(GAMES)-1:0] i = current_game+1; (i < (current_game+1+8'(matched))) && (i < 8'(GAMES)); i++) begin
            games[i] <= games[i] + games[current_game];
        end
        current_game <= current_game + 1;
    end
end

// Sum output
always_ff @(posedge clk_i, negedge rstn_i) begin
    if (!rstn_i) begin
        sum <= '0;
        sum_o <= '0;
    end else if (run_i) begin
        sum <= sum + games[current_game];
    end else begin
        sum_o <= sum;
    end
end

endmodule