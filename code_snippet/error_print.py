
import traceback

sample_list = [1,2,3]

try:
    sample_list[3] = 4
except:
    traceback.print_exc()
