Title: 言うことを聞かないVivado HLSを手なずける
Date: 2015-01-19 23:30:00
Category: 
Tags: HLS
Slug: taming_vivado_hls

[前回]({filename}about_vivado_hls.md)、Vivado HLSにていろいろと問題に遭遇していることを書いたが、
いくらか前進できた。

まず、Co-simulationとC simulationの結果が一致しないという問題。大体以下のような形のコードになっていた。topが合成したい関数のトップレベル。

    :::c
    static int A[] = {...};
    static int B[] = {...};
    
    int g(int* array){
        ....
        use array element
        ....
    }
    
    void f(int* array){
         ....
         g(array);
         ....
    }
    
    void top(){
         ....
         f(A);
         f(A);
         f(B);
         f(B);
         ....
    }

これを、次のように書き換えた。

    :::c
    static int A[] = {...};
    static int B[] = {...};
    
    int g(int* array){
        ....
        use array element
        ....
    }
    
    void f_a(){
         ....
         g(A);
         ....
    }
    
    void f_b(){
         ....
         g(B);
         ....
    }
    
    void top(){
         ....
         f_a();
         f_a();
         f_b();
         f_b();
         ....
    }

f_a, f_bはfと処理は同じだけれど、下位関数に渡す配列を引数にするのではなく、関数内で固定した。これでC simulationと
一致するRTLが生成された。もちろん、いつもこのようにすれば大丈夫という保証はないので一例として理解して欲しい。

これにたどり着くのも色々試行錯誤したのだけれど、間違ったSim結果を見ている限り、A,Bに対するインデックスの生成が
そもそも間違っていたので、なんとなく当たりを付けて等価変換したところ、やっと正しい結果となった。

次に、Co-simが終了しないという問題。こちらは最初の問題よりも対処方法は適当だったが、ある関数にINLINE
ディレクティブを付けると終了するようになった。回路規模としては増大したが、それでもこちらの方が
正しい回路になっているようだ。

この、Co-simが終了しない問題はかなりやっかいだと思った。

なお、Co-simの結果の波形は、Verilogでシミュレーションするとwdb, wcfgというファイルがsim/verilogディレクトリに
できるので、これをVivadoから開けば見ることができる。

いずれにせよ、Vivado HLSを使うには、C simulationだけでなくCo-simulationまでしっかりと動かして
結果を確認することが必須だ。高速でなくてもせめて等価なコードを100%生成して欲しいところだが、
現状そのレベルには達していないようだ。