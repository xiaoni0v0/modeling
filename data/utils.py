import pandas as pd


def read_xls(fp):
    """
    读一个excel文件，返回numpy的array
    """

    df = pd.read_excel(fp)
    return df.to_numpy()


def write_xls(fp, data):
    """
    写一个excel文件，data为numpy的array
    """

    df = pd.DataFrame(data)
    df.to_excel(fp, index=False)
