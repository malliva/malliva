import styles from './app.module.scss';

import { ReactComponent as Logo } from './logo.svg';
import star from './star.svg';

import { Route, Link } from 'react-router-dom';

import { MarketAppLandingPage } from 'libs/market-app/landing-page/src/index';

export function App() {
  return (
    <div>
      <MarketAppLandingPage />
    </div>
  );
}

export default App;
