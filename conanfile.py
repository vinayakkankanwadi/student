from conans import ConanFile, CMake
   
class StudentConan(ConanFile):
   name = "Student"
   version = "0.1"
   license="MIT"
   settings = "os", "compiler", "build_type", "arch"
   exports_sources ="*"

   def source(self):
       tools.replace_in_file("CMakeLists.txt", "PROJECT(Student)", '''PROJECT(Student)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()''')

   def build(self):
       cmake = CMake(self.settings)
       #self.run('cd hello && cmake . %s' % cmake.command_line)
       self.run("cmake --build . %s" % cmake.build_config)

   def package(self):
       self.copy("*.h", dst="include", src="student")
       self.copy("*.lib", dst="lib", src="student/lib")
       self.copy("*.a", dst="lib", src="student/lib")

   def package_info(self):
       self.cpp_info.libs = ["student"]

