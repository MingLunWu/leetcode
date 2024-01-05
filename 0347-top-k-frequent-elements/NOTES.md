**使用 Python 內建語法的暴力版本**

更好的做法是使用 Bucket Sort : 
* 原始版本是透過 n : count(n) 來儲存 / 但壞處是還要在 sort by value
* 優化版本 : 直接透過 count(n): list of num 來儲存。



**Takeway: 這種類型的問題，似乎都要想辦法把關鍵元素放在 Hashmap 的 Key，包含 Grouped anagrams 也是類似解法。**​
