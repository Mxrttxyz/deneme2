import { useState } from 'react';
import { ClipboardCopy } from 'lucide-react';

// Main application component
export default function App() {
  // State to track the copy action
  const [copiedText, setCopiedText] = useState('');
  
  // URL for the profile picture from the uploaded file
  const profilePicUrl = "10478263903257060033.jpg";

  // Function to copy text to the clipboard
  const copyToClipboard = (textToCopy) => {
    try {
      // execCommand method works better within iframes
      const el = document.createElement('textarea');
      el.value = textToCopy;
      document.body.appendChild(el);
      el.select();
      document.execCommand('copy');
      document.body.removeChild(el);

      setCopiedText(textToCopy);
      setTimeout(() => setCopiedText(''), 1500); // Hide the message after 1.5 seconds

    } catch (err) {
      console.error('Copying failed', err);
    }
  };
  
  return (
    <div className="bg-black text-white min-h-screen flex flex-col items-center justify-center p-4">
      <div className="flex flex-col items-center text-center max-w-lg w-full">
        
        {/* Profile photo */}
        <img
          src={profilePicUrl}
          alt="" 
          className="w-36 h-36 rounded-full border-4 border-[#8B0000] mb-6 shadow-lg"
          style={{ filter: 'contrast(1.2) saturate(1.2) brightness(1.1)' }}
        />

        {/* Name and description */}
        <h1 className="text-4xl md:text-5xl font-bold mb-2 text-[#FF0000]" style={{ textShadow: '0 0 10px #ff0000' }}>
          Mxrtt
        </h1>
        <p className="text-lg md:text-xl font-medium mb-8 text-[#FF0000]">
          I don't know what to write here, I was just experimenting and writing code, by the way, my closest friend Ömxr is a complete idiot :D
        </p>
        

        {/* Horizontal line */}
        <div className="w-4/5 h-px bg-gray-500 my-8"></div>

        {/* Icons and text */}
        <div className="flex justify-center items-center gap-6">
          {/* Discord Icon */}
          <div 
            onClick={() => copyToClipboard("reverland.f")}
            className="p-4 rounded-full transition-all transform hover:scale-110 cursor-pointer shadow-lg"
            style={{ backgroundColor: '#000', textShadow: '0 0 15px #ffffff, 0 0 10px #ffffff' }}
            title="Copy Discord" // Tooltip added
          >
            {/* Discord icon image from uploaded file, with cache-busting */}
            <img 
              src={`image_292404.png?v=${new Date().getTime()}`} 
              alt="Discord Icon" 
              className="w-12 h-12 rounded-full"
            />
          </div>

          {/* Spotify Icon */}
          <a 
            href="https://open.spotify.com/user/31kveias72kw5d7ubqjb6jitvexq?si=341bb7f37393429f" 
            target="_blank" 
            rel="noopener noreferrer"
            className="p-4 rounded-full transition-all transform hover:scale-110 cursor-pointer shadow-lg"
            style={{ backgroundColor: '#000', textShadow: '0 0 15px #ffffff, 0 0 10px #ffffff' }}
            title="Go to Spotify" // Tooltip added
          >
            {/* Spotify icon image */}
            <img 
              src="image_276d88.png" 
              alt="Spotify Icon" 
              className="w-12 h-12 rounded-full"
              style={{ filter: 'brightness(2) contrast(1.5)' }}
            />
          </a>
        </div>

        {/* Copied message */}
        {copiedText && (
          <div className="fixed bottom-8 left-1/2 -translate-x-1/2 p-3 px-6 rounded-full bg-gray-700 text-white text-sm shadow-xl transition-all duration-300">
            Copied: {copiedText} <ClipboardCopy size={16} className="inline ml-2" />
          </div>
        )}
      </div>

      {/* Footer / Developer Alias */}
      <footer className="text-center text-gray-500 text-sm mt-8 pb-4 w-full">
        <p>Mxrtt.dev</p>
      </footer>
    </div>
  );
}
