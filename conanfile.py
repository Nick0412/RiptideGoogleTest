from cmd import Cmd
from conans import ConanFile, CMake, tools
from conan.tools.cmake import CMakeToolchain
import os

class RiptideGoogleTestConan(ConanFile):
    name = "RiptideGoogleTest"
    version = "0.1"
    folder_location = "googletest"
    
    def source(self):
        git = tools.Git(folder=self.folder_location)
        git.clone(url="https://github.com/google/googletest.git", branch="main")

    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()
        
    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder=self.folder_location)
        cmake.build()
        
    def package(self):
        self.copy("*.h", dst="include", src="googletest/googletest/include")
        self.copy("*.h", dst="include", src="googletest/googlemock/include")
        self.copy("*.a", dst="lib", keep_path=False)
    
    def package_info(self):
        self.cpp_info.includedirs = ["include"]
        self.cpp_info.libdirs = ["lib"]
        self.cpp_info.libs = ["googletest"]