#!/usr/bin/env python3

import alexa_auth
import alexa_audio_device

def main():
	alexa_audio_device.pulse_init()
	alexa_auth.start()
	try:
		input("Alexa started. Press Enter to exit...\n")
	except KeyboardInterrupt:
		pass
	alexa_auth.close()
	alexa_audio_device.pulse_close()
 
if __name__ == '__main__':
	main()
