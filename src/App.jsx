import React from "react"
import Phishing from './components/phishing'

const App = () => {
  return (
    <>
      <div className="min-h-screen bg-gray-100 flex flex-col items-center">
        <header className="w-full bg-white shadow-md">
          <nav className="container mx-auto flex items-center justify-between py-4 px-6">
            <div className="text-xl font-bold">Spam Analyser</div>
            <button className="bg-gray-800 text-white px-4 py-2 rounded-md">Srinjay Fadikar</button>
          </nav>
        </header>

        <main className="flex-grow flex flex-col items-center justify-center px-6">
          <h1 className="text-4xl font-bold text-center text-gray-800 leading-tight mb-4">
            Phishing Detection: Stay <br /> Vigilant, Avoid Scams
          </h1>
          <p className="text-gray-600 text-center max-w-xl mb-8">
            Discover the latest techniques to identify and prevent phishing
            attacks. Our comprehensive guide covers email verification, URL
            analysis, and social engineering tactics to keep your online activities safe.
          </p>
          <button className="bg-red-500 text-white px-6 py-3 rounded-md shadow-md hover:bg-red-600">
            User Guidelines
          </button>
        </main>
      </div>
      <Phishing/>
    </>
  );
};

export default App;
