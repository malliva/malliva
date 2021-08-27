import React from 'react';
import {
  BrowserRouter as Router,
  Redirect,
  Route,
  Switch,
} from 'react-router-dom';

import styles from './index.module.scss';
import { MarketAppLandingPage } from 'libs/market-app/landing-page/src/index';
import { MarketAppTopMenu } from '@client/market-app/top-menu';

export function Index() {
  const menu = [
    { name: 'Home', link: '#', type: '' },
    { name: 'About', link: '#', type: '' },
    { name: 'Blog', link: '#', type: '' },
    { name: 'Contact us', link: '#', type: '' },
    { name: 'Invite new members', link: '#', type: '' },
  ];

  return (
    <>
      <MarketAppTopMenu menu={menu} />
      <MarketAppLandingPage />
    </>
  );
}

export default Index;
