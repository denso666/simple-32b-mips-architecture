`timescale 1ns/1ns
module buffer_wb (
    input clk,
    input [1:0] in,
    output reg [1:0] out
);

    always @ (posedge clk) out = in;

endmodule // buffer_wb
