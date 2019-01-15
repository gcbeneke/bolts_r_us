
"use strict";

let StopMotion = require('./StopMotion.js')
let StartMotion = require('./StartMotion.js')
let SetRemoteLoggerLevel = require('./SetRemoteLoggerLevel.js')
let GetRobotInfo = require('./GetRobotInfo.js')
let SetDrivePower = require('./SetDrivePower.js')
let CmdJointTrajectory = require('./CmdJointTrajectory.js')

module.exports = {
  StopMotion: StopMotion,
  StartMotion: StartMotion,
  SetRemoteLoggerLevel: SetRemoteLoggerLevel,
  GetRobotInfo: GetRobotInfo,
  SetDrivePower: SetDrivePower,
  CmdJointTrajectory: CmdJointTrajectory,
};
