import styles from './app.module.scss';

import { ReactComponent as Logo } from './logo.svg';
import star from './star.svg';

import { Route, Link } from 'react-router-dom';

import { MarketAppSignUps } from 'libs/market-app/sign-ups/src/index';
import { MarketAppSignIn } from 'libs/market-app/sign-in/src/index';

export function App() {
  return (
    <div>
      <MarketAppSignUps />
      {/* <MarketAppSignIn /> */}
    </div>
  );
}

export default App;
