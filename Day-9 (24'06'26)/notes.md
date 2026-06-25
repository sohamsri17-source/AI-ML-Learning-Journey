### 1. Identifying Missing Data (Detection)

Before fixing gaps, you have to find them. Pandas treats `NaN` (Not a Number) or `None` as missing values.

* **`df.isnull()` / `df.isna()**`: Scans your entire dataset and flags every cell. It outputs a matrix of `True` (missing) and `False` (filled).
* **`df.isnull().sum()`**: The gold standard for data exploration. Because Python treats `True` as 1 and `False` as 0, adding `.sum()` collapses the matrix to give you a clean count of exactly how many missing values exist in each column.


### 2. Dropping Missing Data (Elimination)

When data is corrupted, mostly empty, or critical identifiers (like a user ID or Name) are missing, dropping it is often the safest route.

* **`df.dropna()` (Rows)**: The default behavior. If a row has even *one* missing value, the entire row is deleted.
* *Pro-tip:* Use `df.dropna(subset=['Column'])` to only drop rows if a specific critical column is empty.


* **`df.dropna(axis=1)` (Columns)**: Drops the entire column if it contains a single `NaN`. Use this cautiously, as a single missing cell could wipe out thousands of valid data points in that column.

---

### 3. Filling Missing Data (Imputation)

When deleting data would lose too much valuable information, you "impute" (fill in) the gaps using `df.fillna()`.

* **Scalar Values**: Replaces all `NaN`s with a fixed, static anchor value (e.g., `df.fillna(0)` or `df.fillna('Unknown')`). This is great for keeping the dataset intact without overthinking the math.
* **Statistical Measures**: Replaces `NaN`s using calculations from the rest of the column to maintain statistical integrity:
* **Mean (`.mean()`)**: Fills gaps with the average. Best for symmetric, normally distributed numerical data.
* **Median (`.median()`)**: Fills gaps with the middle value. Best for skewed numerical data heavily influenced by extreme outliers (like income or housing prices).
* **Mode (`.mode()[0]`)**: Fills gaps with the most frequent value. This is the go-to choice for filling in missing categorical data (like favorite color, state of residence, or car model).
