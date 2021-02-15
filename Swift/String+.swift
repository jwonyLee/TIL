// https://gist.github.com/albertbori/0faf7de867d96eb83591#gistcomment-2034215
// String subscript를 도와주는 Extension

import Foundation

extension String {
    subscript(r: Range<Int>) -> String {
        get {
            let startIndex = self.index(self.startIndex, offsetBy: r.lowerBound)
            let endIndex = self.index(self.startIndex, offsetBy: r.upperBound)

            return String(self[startIndex..<endIndex])
        }
    }

    subscript(r: ClosedRange<Int>) -> String {
        get {
            let startIndex = self.index(self.startIndex, offsetBy: r.lowerBound)
            let endIndex = self.index(self.startIndex, offsetBy: r.upperBound)

            return String(self[startIndex...endIndex])
        }
    }
}