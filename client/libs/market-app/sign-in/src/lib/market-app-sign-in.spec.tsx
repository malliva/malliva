import { render } from '@testing-library/react';

import MarketAppSignIn from './market-app-sign-in';

describe('MarketAppSignIn', () => {
  it('should render successfully', () => {
    const { baseElement } = render(<MarketAppSignIn />);
    expect(baseElement).toBeTruthy();
  });
});
