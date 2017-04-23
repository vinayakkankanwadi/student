from conans import ConanFile, CMake, tools
import os


class StudentConan(ConanFile):
    name = "Student"
    version = "0.1"
    license = "<Put the package license here>"
    url = "<Package recipe repository url here, for issues about the package>"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"

    def source(self):
        self.run("git clone https://github.com/vinayakkankanwadi/student.git")
        self.run("cd student")
        # This small hack might be useful to guarantee proper /MT /MD linkage in MSVC
        # if the packaged project doesn't have variables to set it properly
        tools.replace_in_file("student/CMakeLists.txt", "PROJECT(Student)", '''PROJECT(Student)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()''')

    def build(self):
        cmake = CMake(self.settings)
        #shared = "-DBUILD_SHARED_LIBS=ON" if self.options.shared else ""
        #self.run('cmake student %s %s' % (cmake.command_line, shared))
        self.run('cmake student %s' % (cmake.command_line))
        self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        #self.copy("*.h", dst="include", src="student\include")
        self.copy("*student.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)
        self.copy("*.h", dst="include", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["student"]
