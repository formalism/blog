Title: MicroBlaze + IPコア(続き)
Date: 2011-03-18 05:30:00
Category: 
Tags: Programming,FPGA
Slug: microblaze-ip-endian

Create or Import Peripheralで生成されるuser_logic.vhdでは、データバスがstd_logic_vector(0 to 31)で宣言されている。これはMSBがbit0でLSBがbit31となるというMicroBlazeの仕様のため。<a href="http://www.vhdl-online.de/tutorial/englisch/t_58.htm#pgfId-1016798">http://www.vhdl-online.de/tutorial/englisch/t_58.htm#pgfId-1016798</a>を読んで分かったのは、VHDLでインスタンスを宣言するときの配列ポートは、<u>ビット番号ではなく、ビット並びの順番</u>で接続されるということ。
