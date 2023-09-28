
from pyulog.core import ULog

original_path='C:/Users/*.ulg'
write_path='C:/Users/repaired_*.ulg'

log_data = ULog(str(original_path))
log_data.write_ulog(write_path)

