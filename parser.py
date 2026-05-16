import pandas as pd


hw1_df = pd.read_csv('python-2025 - big-hw-01.csv')
hw2_df = pd.read_csv('python-2025 - big-hw-02.csv')

def get_df_by_hw_name(hw_name: str) -> pd.DataFrame:
    if hw_name == 'hw1':
        return hw1_df
    elif hw_name == 'hw2':
        return hw2_df
    else:
        raise ValueError(f"Unknown homework name: {hw_name}")

def get_names():
    names_1 = hw1_df['Unnamed: 0'].tolist()
    names_2 = hw2_df['Unnamed: 0'].tolist()
    names = set(names_1) | set(names_2)
    return list(names)


def get_mean_score_of_hw(hw_name: str) -> float:
    df = get_df_by_hw_name(hw_name)
    count = len(df)
    sum_scores = df['Баллы'].sum()

    mean_score = sum_scores / count
    return mean_score


def get_mean_score_of_hw_in_group(hw_name: str, group_id: str) -> float:

    df = get_df_by_hw_name(hw_name)
    sum = 0
    count = 0

    for tup in df.itertuples():
        if str(int(tup[2])) == group_id:
            count += 1
            sum += int(tup[4])        
    
    if count == 0:
        return 0.0

    return sum / count


def get_student_mark(student_id: int) -> int:
    sum_scores = hw1_df.iloc[student_id]['Баллы'] + hw2_df.iloc[student_id]['Баллы']
   
    if sum_scores < 1:
        return 2
    elif 1 < sum_scores < 30:
        return 3
    elif sum_scores < 50:
        return 4
    return 5

if __name__ == '__main__':
    print(get_mean_score_of_hw_in_group('hw1', '24137'))

    











