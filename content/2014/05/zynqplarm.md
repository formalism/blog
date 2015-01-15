Title: ZynqのPLロジックからARMへの割り込み実験
Date: 2014-05-13 13:32:00
Category: 
Tags: Zynq
Slug: zynq-pl-arm

Zynq上のPLに作成した回路からARMへ割り込むときに、割り込みレイテンシがどれくらいになるのかを計測してみた。

ZYBOを使用しているので、ARMは650MHzで動作。結論は次の画像：<br /><br /><div class="separator" style="clear: both; text-align: center;"><a href="http://1.bp.blogspot.com/-h5KhqquhE_o/U3Idw7Om3vI/AAAAAAAABq8/W7L_-P4Zjhw/s1600/irq.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" src="http://1.bp.blogspot.com/-h5KhqquhE_o/U3Idw7Om3vI/AAAAAAAABq8/W7L_-P4Zjhw/s1600/irq.png" height="227" width="400" /></a></div><br /><br />

1クロックは10ns(100MHz)。一番下のIRQがHighになるとCPUに割り込みがかかる。AXIバスを通してレジスタをクリアするとIRQがLowになる。これを見ると、たったの**31クロック(=310ns)で割り込みがクリアされている**。

これはStandalone(Linuxではなく、ベアメタル)で実験した。割り込みを有効にする部分だけ、参考に貼っておく。
<pre>
Status = XScuGic_Connect(IntcInstancePtr, XPS_FPGA0_INT_ID,(Xil_ExceptionHandler)IrqHandler, NULL);
    if (Status != XST_SUCCESS){
        return Status;
    }
XScuGic_Enable(IntcInstancePtr, XPS_FPGA0_INT_ID);
</pre>

これでXPS_FPGA0_INT_ID(61)番の割り込みが発生すると、 IrqHandler関数が呼ばれる。IrqHandler関数の中で、PLロジックにアクセスして、割り込みをクリアしている。
