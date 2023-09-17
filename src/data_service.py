import json
import os

import pandas as pd


class DataService:
    def __init__(self):
        pass

    def getExcel(self, filename):
        try:
            df = pd.read_excel(f'input/{filename}.xlsx', sheet_name="Sheet1", header=0)
            return df
        except FileNotFoundError:
            raise FileNotFoundError("파일을 찾을 수 없습니다.")
        except Exception:
            raise Exception("알 수 없는 오류가 발생했습니다.")

    def dfToDict(self, df):
        try:
            return df.to_dict("records")
        except AttributeError:
            raise AttributeError("데이터프레임이 아닙니다.")
        except Exception:
            raise Exception("알 수 없는 오류가 발생했습니다.")

    def dictToDf(self, dict):
        try:
            return pd.DataFrame.from_dict(dict)
        except AttributeError:
            raise AttributeError("딕셔너리가 아닙니다.")
        except Exception:
            raise Exception("알 수 없는 오류가 발생했습니다.")

    def dictTOJsonFile(self, dict, filename):
        try:
            # output 폴더가 없으면 생성
            if not os.path.exists("output"):
                os.makedirs("output")
                
            path = f'output/{filename}.json'
            with open(path, "w", encoding="utf-8") as outfile:
                json.dump(dict, outfile, indent=4, ensure_ascii=False)
        except FileNotFoundError:
            raise FileNotFoundError("파일을 찾을 수 없습니다.")
        except Exception:
            raise Exception("알 수 없는 오류가 발생했습니다.")
