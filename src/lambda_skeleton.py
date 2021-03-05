"""
This is a minimal example for a Python script that could be used 1. as a lambda 2. in ECS
"""
import os
from typing import TypedDict,Dict,Any, Final,Union
from pydantic import BaseModel
import json
import argparse
import logging
import datetime

# ENVIRONMENT VARIABLES AND GLOBAL PARAMETERS
service_name = "transform_data"
env = os.getenv("ENVIRONMENT", "dev")
testing: Final[Union[bool, str]] = os.getenv("TESTING", False)
# SETUP LOGGING
log_level: str = os.getenv("LOGLEVEL", "INFO").upper()
logging.getLogger().setLevel(log_level)
logging.basicConfig(level=log_level)
logger = logging.getLogger(__name__)

class HandlerResult(TypedDict):
  statusCode:int
  body: str 

class InputEvent(BaseModel):
  source: str
  date: str


def handler(input_event: Dict[str, Any], context: Any = None) -> HandlerResult:
  """
  Lambda entrypoint. Transforms the data in S3 
  """
  logger.info(f"Running in env {env}")
  e = InputEvent(**input_event)
  logger.info(f"Input payload is {e}")
  return {
      "statusCode":
          200,
      "body":
          json.dumps(
              f"Completed lambda"
          )
  }

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("--input", help="payload for the function handler")
  args = parser.parse_args()
  logger.info(args.input)
  # LOAD DATA FROM TESTING FILE IF ENVIRONMENT VARIABLE TESTING IS SET AND NO INPUT ARGUMENTS
  raw_event: Dict[str, Any] = args.input if not testing else {"source":"test","date":"2020-01-02"}
  handler(input_event=raw_event)

if __name__ == '__main__':
  main()
