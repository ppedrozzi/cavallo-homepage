#!/usr/bin/env python3
"""
Resize images in pictures/ directory to max 1400px width while maintaining aspect ratio.

Usage:
    python3 resize_images.py

Requirements:
    Pillow library (pip3 install --user pillow --upgrade)

Output:
    Images saved to pictures-resized-temp/ directory with same structure
"""

from PIL import Image
import os
import glob
import sys


def resize_image(img_path, target_width=1400):
    """Resize image if width exceeds target_width, maintain aspect ratio."""
    try:
        img = Image.open(img_path)
        rel_path = os.path.relpath(img_path, start="pictures")
        output_path = os.path.join("pictures-resized-temp", rel_path)
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        if img.width > target_width:
            # Calculate new height maintaining aspect ratio
            height = int((target_width / img.width) * img.height)
            img = img.resize((target_width, height), Image.Resampling.LANCZOS)
            action = "🎨 REZISED"
            processed = True
        else:
            action = "✅ KEEP"
            processed = False
        
        # Save with appropriate compression based on format
        if img_path.lower().endswith('.webp'):
            img.save(output_path, 'WEBP', quality=85, method=6)
        elif img_path.lower().endswith(('.jpg', '.jpeg')):
            img.save(output_path, 'JPEG', quality=85, optimize=True, progressive=True)
        else:
            img.save(output_path)
            
        return {
            'rel_path': rel_path,
            'action': action,
            'output_path': output_path,
            'original_size': f"[{img.width if processed else f"{img.width}x{img.height}":>4}",
            'new_size': f"[{img.width}x{img.height}]" if processed else "Same",
            'success': True
        }
        
    except Exception as e:
        return {
            'rel_path': os.path.relpath(img_path, start="pictures"),
            'action': "❌ ERROR",
            'output_path': None,
            'original_size': "N/A",
            'new_size': str(e)[:40],
            'success': False
        }


def main(target_width=1400):
    """Main resize function."""
    processed_count = 0
    skipped_count = 0
    error_count = 0
    
    # All image formats supported by Pillow
    image_extensions = ['*.png', '*.jpg', '*.jpeg', '*.gif', '*.bmp', '*.tiff', '*.webp']
    image_files = []
    
    print(f"\n🔄 Starting image resize procedure...\n")
    
    # Find all image files
    for ext in image_extensions:
        image_files.extend(glob.glob(f"pictures/**/{ext}", recursive=True))
    
    if not image_files:
        print("⚠️ No images found in pictures/ directory\n")
        return 1
    
    print(f"Found {len(image_files)} images in pictures/ directory")
    print(f"Target max width: {target_width}px\n")
    print(f"{'File Path':<60} {'Action':<10} {'Size':>15}")
    print(f"{'-'*90}\n")
    
    results = []
    
    # Process each image
    for img_path in sorted(image_files):
        result = resize_image(img_path, target_width)
        results.append(result)
        
        if result['action'] == "🎨 REZISED":
            print(f"{result['rel_path']:<60} {result['action']:<10} {result['new_size']:>15}")
            processed_count += 1
        elif result['action'] == "✅ KEEP":
            print(f"{result['rel_path']:<60} {result['action']:<10} {result['original_size']:>15}")
            skipped_count += 1
        else:  # Error
            print(f"{result['rel_path']:<60} {result['action']:<10} ⚠️  {result['new_size']:>4}")
            error_count += 1
    
    print(f"\n{'-'*90}\n")
    
    # Summary
    total = processed_count + skipped_count + error_count
    print(f"✨ RESIZE PROCEDURE COMPLETE!")
    print(f"   Total images: {total}")
    print(f"   - Resized:   {processed_count} ({processed_count/total*100:.1f}%)")
    print(f"   - Skipped:   {skipped_count} ({skipped_count/total*100:.1f}%)")
    print(f"   - Errors:    {error_count} ({error_count/total*100:.1f}%)")
    print()
    
    if processed_count > 0:
        print(f"✅ Output directory: pictures-resized-temp/ ({len(results)} files)")
    
    if error_count > 0:
        print(f"\n⚠️  {error_count} errors occurred. Check output above.")
        return 1
    
    return 0


if __name__ == "__main__":
    # Navigate to script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    # Check if Pillow is available
    try:
        from PIL import Image
        print(f"✅ Pillow version: {Image.__version__}\n")
    except ImportError:
        print("❌ ERROR: Pillow library not installed!")
        print("Install with: pip3 install --user pillow --upgrade\n")
        sys.exit(1)
    
    # Run main function
    sys.exit(main(target_width=1400))