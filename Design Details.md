<!--
 * @Author: Lucas Wye<lucas.zw.ye@outlook.com>
 * @Date: 2020-12-25 11:19:45
-->
## Design Details
```
ALUCtrl_i [2:0]
parameter SUM = 3'b001;
parameter SUB = 3'b010;
parameter AND = 3'b011;
parameter OR  = 3'b100;
parameter XOR = 3'b101;
parameter MUL = 3'b110;


7'b0010011 : begin //addi
7'b0110011 : begin //others
7'b1100011 : begin //beq
7'b0000011 : begin //lw
7'b0100011 : begin //sw
7'b1010111: begin //vector
```