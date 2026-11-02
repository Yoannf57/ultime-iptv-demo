// Dessine les logos des chaînes de démonstration (logos/demo1.png …).
// Formes et texte uniquement, aucune marque : ces images sont placées dans le domaine public (CC0).
// Usage (sur un Mac) : swift outils/logos.swift logos
import AppKit

let output = CommandLine.arguments.count > 1 ? CommandLine.arguments[1] : "logos"
let size = 512

struct Logo {
    let file: String
    let label: String
    let color: NSColor
}

let logos = [
    Logo(file: "demo1", label: "1", color: NSColor(srgbRed: 0.35, green: 0.78, blue: 0.98, alpha: 1)),
    Logo(file: "demo2", label: "2", color: NSColor(srgbRed: 0.96, green: 0.65, blue: 0.14, alpha: 1)),
    Logo(file: "demo3", label: "3", color: NSColor(srgbRed: 0.20, green: 0.83, blue: 0.60, alpha: 1)),
    Logo(file: "demo4", label: "4", color: NSColor(srgbRed: 0.65, green: 0.55, blue: 0.98, alpha: 1)),
]

func draw(_ logo: Logo) throws {
    guard let rep = NSBitmapImageRep(
        bitmapDataPlanes: nil, pixelsWide: size, pixelsHigh: size, bitsPerSample: 8, samplesPerPixel: 4,
        hasAlpha: true, isPlanar: false, colorSpaceName: .deviceRGB, bytesPerRow: 0, bitsPerPixel: 0)
    else { throw NSError(domain: "logos", code: 1) }
    NSGraphicsContext.saveGraphicsState()
    NSGraphicsContext.current = NSGraphicsContext(bitmapImageRep: rep)
    let s = CGFloat(size)

    NSColor(srgbRed: 0.08, green: 0.08, blue: 0.09, alpha: 1).setFill()
    NSBezierPath(rect: NSRect(x: 0, y: 0, width: s, height: s)).fill()

    // Disque de couleur avec le numéro.
    let disc = NSRect(x: s * 0.22, y: s * 0.30, width: s * 0.56, height: s * 0.56)
    logo.color.setFill()
    NSBezierPath(ovalIn: disc).fill()
    let digit = NSAttributedString(string: logo.label, attributes: [
        .font: NSFont.systemFont(ofSize: s * 0.36, weight: .heavy),
        .foregroundColor: NSColor(srgbRed: 0.08, green: 0.08, blue: 0.09, alpha: 1),
    ])
    let d = digit.size()
    digit.draw(at: NSPoint(x: disc.midX - d.width / 2, y: disc.midY - d.height / 2))

    let word = NSAttributedString(string: "DEMO", attributes: [
        .font: NSFont.systemFont(ofSize: s * 0.12, weight: .bold),
        .foregroundColor: NSColor.white,
        .kern: s * 0.02,
    ])
    let w = word.size()
    word.draw(at: NSPoint(x: (s - w.width) / 2, y: s * 0.09))

    NSGraphicsContext.restoreGraphicsState()
    guard let png = rep.representation(using: .png, properties: [:]) else { throw NSError(domain: "logos", code: 2) }
    try png.write(to: URL(fileURLWithPath: output).appendingPathComponent(logo.file + ".png"))
}

for logo in logos { try draw(logo) }
print("\(logos.count) logos écrits dans \(output)/")
