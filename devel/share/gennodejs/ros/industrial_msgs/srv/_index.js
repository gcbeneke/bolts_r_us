
"use strict";

let StopMotion = require('./StopMotion.js')
let SetDrivePower = require('./SetDrivePower.js')
let CmdJointTrajectory = require('./CmdJointTrajectory.js')
let StartMotion = require('./StartMotion.js')
let SetRemoteLoggerLevel = require('./SetRemoteLoggerLevel.js')
let GetRobotInfo = require('./GetRobotInfo.js')

module.exports = {
  StopMotion: StopMotion,
  SetDrivePower: SetDrivePower,
  CmdJointTrajectory: CmdJointTrajectory,
  StartMotion: StartMotion,
  SetRemoteLoggerLevel: SetRemoteLoggerLevel,
  GetRobotInfo: GetRobotInfo,
};
