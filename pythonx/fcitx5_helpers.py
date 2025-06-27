import threading
import subprocess
import vim

def fcitx5_get_imname():
	result = subprocess.run(["fcitx5-remote", "-n"], 
                       stdout=subprocess.PIPE, 
                       stderr=subprocess.PIPE,
                       text=True)

	if result.returncode == 0:
		return result.stdout.strip()
	#else:
	#   print("获取输入法失败:", result.stderr)

def fcitx5_record_imname():
	vim.current.buffer.vars["text_fcitx_imname"] = fcitx5_get_imname()

def fcitx5_activate():
	subprocess.Popen(["fcitx5-remote", "-o"])

def fcitx5_record_and_inactivate():
	fcitx5_record_imname()
	subprocess.Popen(["fcitx5-remote", "-c"])

def fcitx5_use_im(imname):
	timer = threading.Timer(0.05, fcitx5_activate)
	timer.start()

def fcitx5_retain_im():
	if fcitx5_get_imname() != vim.current.buffer.vars["text_fcitx_imname"]:
		fcitx5_use_im(vim.current.buffer.vars["text_fcitx_imname"])


