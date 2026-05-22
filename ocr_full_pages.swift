import Foundation
import Vision
import AppKit

func recognizeText(in imagePath: String) {
    let url = URL(fileURLWithPath: imagePath)
    guard let imageSource = CGImageSourceCreateWithURL(url as CFURL, nil),
          let image = CGImageSourceCreateImageAtIndex(imageSource, 0, nil) else {
        print("Failed to load image \(imagePath)")
        return
    }
    
    let requestHandler = VNImageRequestHandler(cgImage: image, options: [:])
    let request = VNRecognizeTextRequest { request, error in
        guard let observations = request.results as? [VNRecognizedTextObservation] else { return }
        print("--- OCR for FULL PAGE: \(url.lastPathComponent) ---")
        var lines = [String]()
        for observation in observations {
            if let candidate = observation.topCandidates(1).first {
                lines.append(candidate.string)
            }
        }
        print(lines.joined(separator: "\n"))
        print("==================================================\n")
    }
    request.recognitionLevel = .accurate
    do {
        try requestHandler.perform([request])
    } catch {
        print("Error: \(error)")
    }
}

let paths = [
    "/Users/joey/reports/nab_figure_drawing/form_02/p8_IMG_2995.HEIC",
    "/Users/joey/reports/nab_figure_drawing/form_02/p9_IMG_2996.HEIC",
    "/Users/joey/reports/nab_figure_drawing/form_02/p7_IMG_2997.HEIC"
]

for path in paths {
    recognizeText(in: path)
}
