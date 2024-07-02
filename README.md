## Решения задачи 44

### Условие задачи

Вам дан код, генерирующий DataFrame, который состоит всего из 1 столбца. Ваша задача - перевести его в one hot вид без использования функции `get_dummies()`.

```python
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
data.head()
