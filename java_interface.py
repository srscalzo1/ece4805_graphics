import os
from jnius import autoclass

# Set CLASSPATH to include JAR
os.environ['CLASSPATH'] = 'java_files/blue-sentinel-app-1.0-SNAPSHOT.jar'

parser_channel = autoclass('ParserChannel.class')

parser = parser_channel()
