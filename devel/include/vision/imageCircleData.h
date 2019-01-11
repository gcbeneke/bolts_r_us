// Generated by gencpp from file vision/imageCircleData.msg
// DO NOT EDIT!


#ifndef VISION_MESSAGE_IMAGECIRCLEDATA_H
#define VISION_MESSAGE_IMAGECIRCLEDATA_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <vision/VectorData.h>

namespace vision
{
template <class ContainerAllocator>
struct imageCircleData_
{
  typedef imageCircleData_<ContainerAllocator> Type;

  imageCircleData_()
    : vector_name()
    , allHolesDataVec()  {
    }
  imageCircleData_(const ContainerAllocator& _alloc)
    : vector_name(_alloc)
    , allHolesDataVec(_alloc)  {
  (void)_alloc;
    }



   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _vector_name_type;
  _vector_name_type vector_name;

   typedef std::vector< ::vision::VectorData_<ContainerAllocator> , typename ContainerAllocator::template rebind< ::vision::VectorData_<ContainerAllocator> >::other >  _allHolesDataVec_type;
  _allHolesDataVec_type allHolesDataVec;





  typedef boost::shared_ptr< ::vision::imageCircleData_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::vision::imageCircleData_<ContainerAllocator> const> ConstPtr;

}; // struct imageCircleData_

typedef ::vision::imageCircleData_<std::allocator<void> > imageCircleData;

typedef boost::shared_ptr< ::vision::imageCircleData > imageCircleDataPtr;
typedef boost::shared_ptr< ::vision::imageCircleData const> imageCircleDataConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::vision::imageCircleData_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::vision::imageCircleData_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace vision

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {'std_msgs': ['/opt/ros/melodic/share/std_msgs/cmake/../msg'], 'vision': ['/home/gijs/bolts_ws/src/vis/vision/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::vision::imageCircleData_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::vision::imageCircleData_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::vision::imageCircleData_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::vision::imageCircleData_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::vision::imageCircleData_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::vision::imageCircleData_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::vision::imageCircleData_<ContainerAllocator> >
{
  static const char* value()
  {
    return "f8a2a99d547045d060df3120b6af8431";
  }

  static const char* value(const ::vision::imageCircleData_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xf8a2a99d547045d0ULL;
  static const uint64_t static_value2 = 0x60df3120b6af8431ULL;
};

template<class ContainerAllocator>
struct DataType< ::vision::imageCircleData_<ContainerAllocator> >
{
  static const char* value()
  {
    return "vision/imageCircleData";
  }

  static const char* value(const ::vision::imageCircleData_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::vision::imageCircleData_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# Message file which can be used to transfer a vector of circle data. For more info see VectorData.msg\n\
# Date: 04-12-2018\n\
# By: Giel Oomen\n\
\n\
string vector_name		# Name of the vector\n\
VectorData[] allHolesDataVec	# Vector of 'VectorData' structs (from VectorData.msg)\n\
\n\
\n\
================================================================================\n\
MSG: vision/VectorData\n\
# This message contains the structure of which the vector in imageCircleData.msg is made of. \n\
# One place in the vector contains x, y, z and size values of one circle detected in the image.\n\
# Date: 04-12-2018	\n\
# By Giel Oomen\n\
\n\
float64 x	# Circle position on x-axis\n\
float64 y	# Circle position on y-axis\n\
float64 z	# Circle position on z-axis (depth in meters)\n\
float64 size	# Circle size \n\
";
  }

  static const char* value(const ::vision::imageCircleData_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::vision::imageCircleData_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.vector_name);
      stream.next(m.allHolesDataVec);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct imageCircleData_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::vision::imageCircleData_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::vision::imageCircleData_<ContainerAllocator>& v)
  {
    s << indent << "vector_name: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.vector_name);
    s << indent << "allHolesDataVec[]" << std::endl;
    for (size_t i = 0; i < v.allHolesDataVec.size(); ++i)
    {
      s << indent << "  allHolesDataVec[" << i << "]: ";
      s << std::endl;
      s << indent;
      Printer< ::vision::VectorData_<ContainerAllocator> >::stream(s, indent + "    ", v.allHolesDataVec[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // VISION_MESSAGE_IMAGECIRCLEDATA_H
