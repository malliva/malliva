import React from 'react';
import { AppProps } from 'next/app';
import Head from 'next/head';
import { ReactComponent as NxLogo } from '../public/nx-logo-white.svg';
import './styles.css';

import { Provider } from 'react-redux';
import { PersistGate } from 'redux-persist/integration/react';
import { persistor, store } from '../store';

function CustomApp({ Component, pageProps }: AppProps) {
  return (
    <>
      <Head>
        <title>Welcome to market-nx-app!</title>
      </Head>
      <div className="app">
        <main>
          <Provider store={store}>
            <PersistGate persistor={persistor}>
              <Component {...pageProps} />
            </PersistGate>
          </Provider>
        </main>
      </div>
    </>
  );
}

export default CustomApp;
