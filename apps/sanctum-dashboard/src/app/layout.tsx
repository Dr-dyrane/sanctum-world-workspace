import type { Metadata } from 'next';
import type { ReactNode } from 'react';
import './globals.css';

export const metadata: Metadata = {
  title: 'Sanctum Dashboard',
  description: 'Clinical world and task cockpit',
  robots: {
    index: false,
    follow: false,
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: ReactNode;
}>) {
  const loadDesignCdns = process.env.NODE_ENV === 'production';

  return (
    <html lang="en">
      <head>
        {loadDesignCdns ? (
          <>
            <script dangerouslySetInnerHTML={{ __html: "window.tailwind = window.tailwind || {}; window.tailwind.config = { darkMode: 'class' };" }} />
            <script src="https://cdn.tailwindcss.com" defer />
            <script src="https://unpkg.com/lucide@latest/dist/umd/lucide.min.js" defer />
          </>
        ) : null}
      </head>
      <body>
        {children}
      </body>
    </html>
  );
}
