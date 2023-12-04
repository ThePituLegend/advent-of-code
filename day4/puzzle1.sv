/*
 * Advent of Code 2023 - Day 4
 * Puzzle 1
 *
 * The module receives a list of winning numbers, and a list of played numbers, each cycle (a game).
 * Each game gets its score as 2^(i-1), where i is the number of winning numbers that were played
 *  (1 match = 1 point, double each additional match).
 * The module outputs the sum of all scores.
*/

`timescale 1us/1ns

module puzzle1
#(
    parameter int WINNING_NUMBERS = 10,
              int PLAYED_NUMBERS = 25
)
(
    input logic clk_i,
    input logic rstn_i,
    input logic run_i,
    input logic [WINNING_NUMBERS-1:0][6:0] winning_numbers_i,
    input logic [PLAYED_NUMBERS-1:0][6:0] played_numbers_i,
    output logic [31:0] sum_o
);

logic [31:0] game_score;
logic [31:0] sum;

always_comb begin
    game_score = 0;
    if (run_i) begin
        for (int i = 0; i < WINNING_NUMBERS; i++) begin
            for (int j = 0; j < PLAYED_NUMBERS; j++) begin
                if (winning_numbers_i[i] == played_numbers_i[j]) begin
                    if (game_score == 0) begin
                        game_score = 1;
                    end else begin
                        game_score <<= 1;
                    end
                end
            end
        end
    end
end

// Sum output
always_ff @(posedge clk_i, negedge rstn_i)
begin
    if (!rstn_i) begin
        sum <= '0;
        sum_o <= '0;
    end else if (run_i) begin
        sum <= sum + game_score;
    end else begin
        sum_o <= sum;
    end
end

endmodule