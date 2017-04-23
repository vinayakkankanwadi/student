from conans import ConanFile, CMake
import os


channel = os.getenv("CONAN_CHANNEL", "testing")
username = os.getenv("CONAN_USERNAME", "demo")


class StudentTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    requires = "Student/0.1@%s/%s" % (username, channel)
    generators = "cmake"

    def build(self):
        cmake = CMake(self.settings)
        # Current dir is "test_package/build/<build_id>" and CMakeLists.txt is in "test_package"
        cmake.configure(self, source_dir=self.conanfile_directory, build_dir="./")
        cmake.build(self)

    def imports(self):
        self.copy("*.a", "lib", "lib")
        self.copy("*.h", "include", "include")
        self.copy("*.dylib", "bin", "bin")

    def test(self):
        os.chdir("bin")
        self.run(".%sexample" % os.sep)
