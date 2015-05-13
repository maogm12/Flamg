# Flamg

The flames of youth are raging.

## 解题口诀

	动规递归是神器，
	全无用处想哈希。
	先用暴力得初解，
	再据题意破玄奇。

	贪心大法出身好，
	正确路线永不倒。
	二叉树中层次多，
	递归回溯唱凯歌。

## Achievement
<style>
.block {
    display: inline-block;
    width: 20px;
    height: 20px;
    margin: 0;
    padding: 0;
    background-color: lightgray;
    border-right: 1px solid white;
}

.checked {
    background-color: deeppink;
}
</style>
    
<div><!--
 --><span class="block checked"></span><!--
 --><span class="block checked"></span><!--
 --><span class="block checked"></span><!--
 --><span class="block checked"></span><!--
 --><span class="block checked"></span><!--
 --><span class="block checked"></span><!--
 --><span class="block checked"></span><!--
 --><span class="block checked"></span><!--
 --><span class="block checked"></span><!--
 --><span class="block checked"></span><!--
 --><span class="block checked"></span><!--
 --><span class="block "></span><!--
 --><span class="block "></span><!--
 --><span class="block checked"></span><!--
 --><span class="block checked"></span><!--
 --><span class="block checked"></span><!--
 --><span class="block checked"></span><!--
 --><span class="block checked"></span><!--
 --><span class="block checked"></span><!--
 --><span class="block "></span><!--
 --><span class="block "></span><!--
 --><span class="block checked"></span><!--
 --><span class="block "></span><!--
 --><span class="block checked"></span><!--
 --><span class="block checked"></span><!--
 --><span class="block checked"></span><!--
 --><span class="block checked"></span><!--
 --><span class="block checked"></span><!--
 --><span class="block "></span><!--
 --><span class="block "></span><!--
 --><span class="block checked"></span><!--
 --><span class="block "></span><!--
 --><span class="block checked"></span><!--
 --><span class="block "></span><!--
 --><span class="block "></span><!--
 --><span class="block checked"></span><!--
 --><span class="block "></span><!--
 --><span class="block "></span><!--
 --><span class="block checked"></span><!--
 --><span class="block checked"></span><!--
 --><span class="block "></span><!--
 --><span class="block checked"></span><!--
 --><span class="block "></span><!--
 --><span class="block "></span><!--
 --><span class="block checked"></span><!--
 --><span class="block checked"></span><!--
 --><span class="block checked"></span><!--
 --><span class="block checked"></span><!--
 --><span class="block checked"></span><!--
 --><span class="block checked"></span><!--
 --><span class="block checked"></span><!--
 --><span class="block checked"></span><!--
 --><span class="block checked"></span><!--
 --><span class="block checked"></span><!--
 --><span class="block checked"></span><!--
 --><span class="block checked"></span><!--
 --><span class="block checked"></span><!--
 --><span class="block checked"></span><!--
 --><span class="block checked"></span><!--
 --><span class="block checked"></span><!--
 --><span class="block checked"></span><!--
 --><span class="block checked"></span><!--
 --><span class="block checked"></span><!--
 --><span class="block checked"></span><!--
 --><span class="block "></span><!--
 --><span class="block checked"></span><!--
 --><span class="block checked"></span><!--
 --><span class="block checked"></span><!--
 --><span class="block checked"></span><!--
 --><span class="block checked"></span><!--
 --><span class="block "></span><!--
 --><span class="block checked"></span><!--
 --><span class="block checked"></span><!--
 --><span class="block "></span><!--
 --><span class="block "></span><!--
 --><span class="block "></span><!--
 --><span class="block checked"></span><!--
 --><span class="block checked"></span><!--
 --><span class="block checked"></span><!--
 --><span class="block checked"></span><!--
 --><span class="block checked"></span><!--
 --><span class="block checked"></span><!--
 --><span class="block checked"></span><!--
 --><span class="block "></span><!--
 --><span class="block "></span><!--
 --><span class="block checked"></span><!--
 --><span class="block "></span><!--
 --><span class="block "></span><!--
 --><span class="block checked"></span><!--
 --><span class="block checked"></span><!--
 --><span class="block checked"></span><!--
 --><span class="block checked"></span><!--
 --><span class="block "></span><!--
 --><span class="block checked"></span><!--
 --><span class="block checked"></span><!--
 --><span class="block checked"></span><!--
 --><span class="block "></span><!--
 --><span class="block checked"></span><!--
 --><span class="block checked"></span><!--
 --><span class="block checked"></span><!--
 --><span class="block checked"></span><!--
 --><span class="block checked"></span><!--
 --><span class="block checked"></span><!--
 --><span class="block checked"></span><!--
 --><span class="block checked"></span><!--
 --><span class="block checked"></span><!--
 --><span class="block checked"></span><!--
 --><span class="block checked"></span><!--
 --><span class="block checked"></span><!--
 --><span class="block checked"></span><!--
 --><span class="block checked"></span><!--
 --><span class="block checked"></span><!--
 --><span class="block checked"></span><!--
 --><span class="block checked"></span><!--
 --><span class="block checked"></span><!--
 --><span class="block checked"></span><!--
 --><span class="block checked"></span><!--
 --><span class="block "></span><!--
 --><span class="block "></span><!--
 --><span class="block checked"></span><!--
 --><span class="block checked"></span><!--
 --><span class="block checked"></span><!--
 --><span class="block "></span><!--
 --><span class="block checked"></span><!--
 --><span class="block checked"></span><!--
 --><span class="block "></span><!--
 --><span class="block "></span><!--
 --><span class="block checked"></span><!--
 --><span class="block checked"></span><!--
 --><span class="block "></span><!--
 --><span class="block "></span><!--
 --><span class="block "></span><!--
 --><span class="block "></span><!--
 --><span class="block checked"></span><!--
 --><span class="block checked"></span><!--
 --><span class="block checked"></span><!--
 --><span class="block checked"></span><!--
 --><span class="block checked"></span><!--
 --><span class="block checked"></span><!--
 --><span class="block checked"></span><!--
 --><span class="block checked"></span><!--
 --><span class="block checked"></span><!--
 --><span class="block checked"></span><!--
 --><span class="block checked"></span><!--
 --><span class="block checked"></span><!--
 --><span class="block checked"></span><!--
 --><span class="block "></span><!--
 --><span class="block "></span><!--
 --><span class="block "></span><!--
 --><span class="block "></span><!--
 --><span class="block "></span><!--
 --><span class="block "></span><!--
 --><span class="block "></span><!--
 --><span class="block "></span><!--
 --><span class="block "></span><!--
 --><span class="block "></span><!--
 --><span class="block "></span><!--
 --><span class="block "></span><!--
 --><span class="block "></span><!--
 --><span class="block "></span><!--
 --><span class="block "></span><!--
 --><span class="block "></span><!--
 --><span class="block "></span><!--
 --><span class="block "></span><!--
 --><span class="block "></span><!--
 --><span class="block "></span><!--
 --><span class="block "></span><!--
 --><span class="block "></span><!--
 --><span class="block "></span><!--
 --><span class="block "></span><!--
 --><span class="block "></span><!--
 --><span class="block "></span><!--
 --><span class="block "></span><!--
 --><span class="block "></span><!--
 --><span class="block "></span><!--
 --><span class="block "></span><!--
 --><span class="block "></span><!--
 --><span class="block "></span><!--
 --><span class="block "></span><!--
 --><span class="block "></span><!--
 --><span class="block "></span><!--
 --><span class="block "></span><!--
 --><span class="block "></span><!--
 --><span class="block "></span><!--
 --><span class="block "></span><!--
 --><span class="block "></span><!--
 --><span class="block "></span><!--
 --><span class="block "></span><!--
 --><span class="block "></span><!--
 --><span class="block "></span><!--
 --><span class="block "></span><!--
 --><span class="block "></span><!--
 --><span class="block "></span><!--
 --><span class="block "></span><!--
 --><span class="block "></span><!--
 --><span class="block "></span><!--
 --><span class="block "></span><!--
 --><span class="block "></span><!--
 --><span class="block "></span><!--
 --><span class="block "></span><!--
 --><span class="block "></span><!--
 --></div>