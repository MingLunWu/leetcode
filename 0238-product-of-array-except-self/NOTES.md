透過 Prefix 和 Postfix 來儲存每一個 Element 的 prefix product 和 postfix product
最後再將兩個相乘即可。

pseudo code: 

```
prefix[0] = 1
prefix[i] = product of 0 ~ i-1

postfix[end] = 1
postfix[i] = product of i+1 ~ end

result[i] = prefix[i] * postfix[i]
```
