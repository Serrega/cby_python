import platform
import speedtest

print('Platform type: ', platform.platform())
print('Processor: ', platform.processor())
print('Compiler: ', platform.python_compiler())
print('Python version: ', platform.python_version())

s = speedtest.Speedtest()
print('\ndownload: ', round(s.download()/(8*1024**2), 2))
print('upload: ', round(s.upload()/(8*1024**2), 2))


