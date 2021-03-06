// Generated by gencpp from file ctrl/State.msg
// DO NOT EDIT!


#ifndef CTRL_MESSAGE_STATE_H
#define CTRL_MESSAGE_STATE_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace ctrl
{
template <class ContainerAllocator>
struct State_
{
  typedef State_<ContainerAllocator> Type;

  State_()
    : state(0)  {
    }
  State_(const ContainerAllocator& _alloc)
    : state(0)  {
  (void)_alloc;
    }



   typedef int64_t _state_type;
  _state_type state;





  typedef boost::shared_ptr< ::ctrl::State_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::ctrl::State_<ContainerAllocator> const> ConstPtr;

}; // struct State_

typedef ::ctrl::State_<std::allocator<void> > State;

typedef boost::shared_ptr< ::ctrl::State > StatePtr;
typedef boost::shared_ptr< ::ctrl::State const> StateConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::ctrl::State_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::ctrl::State_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace ctrl

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'std_msgs': ['/opt/ros/melodic/share/std_msgs/cmake/../msg'], 'ctrl': ['/home/gijs/bolts_ws/src/ctrl/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::ctrl::State_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::ctrl::State_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::ctrl::State_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::ctrl::State_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ctrl::State_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ctrl::State_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::ctrl::State_<ContainerAllocator> >
{
  static const char* value()
  {
    return "979940cbf4c11dcaa39d4ce8683ecc86";
  }

  static const char* value(const ::ctrl::State_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x979940cbf4c11dcaULL;
  static const uint64_t static_value2 = 0xa39d4ce8683ecc86ULL;
};

template<class ContainerAllocator>
struct DataType< ::ctrl::State_<ContainerAllocator> >
{
  static const char* value()
  {
    return "ctrl/State";
  }

  static const char* value(const ::ctrl::State_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::ctrl::State_<ContainerAllocator> >
{
  static const char* value()
  {
    return "int64 state\n\
";
  }

  static const char* value(const ::ctrl::State_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::ctrl::State_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.state);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct State_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::ctrl::State_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::ctrl::State_<ContainerAllocator>& v)
  {
    s << indent << "state: ";
    Printer<int64_t>::stream(s, indent + "  ", v.state);
  }
};

} // namespace message_operations
} // namespace ros

#endif // CTRL_MESSAGE_STATE_H
