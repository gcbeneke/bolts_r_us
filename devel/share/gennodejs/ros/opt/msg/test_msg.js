// Auto-generated. Do not edit!

// (in-package opt.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class test_msg {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.offSet = null;
    }
    else {
      if (initObj.hasOwnProperty('offSet')) {
        this.offSet = initObj.offSet
      }
      else {
        this.offSet = new Array(6).fill(0);
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type test_msg
    // Check that the constant length array field [offSet] has the right length
    if (obj.offSet.length !== 6) {
      throw new Error('Unable to serialize array field offSet - length must be 6')
    }
    // Serialize message field [offSet]
    bufferOffset = _arraySerializer.float64(obj.offSet, buffer, bufferOffset, 6);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type test_msg
    let len;
    let data = new test_msg(null);
    // Deserialize message field [offSet]
    data.offSet = _arrayDeserializer.float64(buffer, bufferOffset, 6)
    return data;
  }

  static getMessageSize(object) {
    return 48;
  }

  static datatype() {
    // Returns string type for a message object
    return 'opt/test_msg';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'e800213d1d061d690a2ce91f4c737f6b';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float64[6] offSet
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new test_msg(null);
    if (msg.offSet !== undefined) {
      resolved.offSet = msg.offSet;
    }
    else {
      resolved.offSet = new Array(6).fill(0)
    }

    return resolved;
    }
};

module.exports = test_msg;
